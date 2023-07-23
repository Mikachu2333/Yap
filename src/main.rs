use std::io::stdin;
use std::path::Path;
use std::time::{Duration, Instant, SystemTime};
use std::env;
use std::f32;
use std::fs;
use std::path::PathBuf;


use yap::capture;
use yap::common;
use yap::info;
use yap::pickupper::pickup_scanner::PickupScanner;

use image::imageops::grayscale;
use image::{DynamicImage, ImageBuffer, Pixel};
use imageproc::template_matching;

use image::{open, GenericImage, GrayImage, Luma, Rgb, RgbImage};
use imageproc::definitions::Image;
use imageproc::drawing::draw_hollow_rect_mut;
use imageproc::map::map_colors;
use imageproc::rect::Rect;
use imageproc::template_matching::{find_extremes, match_template, MatchTemplateMethod};

use winapi::um::winuser::{SetForegroundWindow, GetDpiForSystem, SetThreadDpiAwarenessContext, ShowWindow, SW_SHOW, SW_RESTORE, GetSystemMetrics, SetProcessDPIAware};

use clap::{Arg, App};

use env_logger::{Env, Builder, Target};
use log::{info, LevelFilter, warn};



fn main() {
    Builder::new().filter_level(LevelFilter::Info).init();


    if !common::is_admin() {
        common::error_and_quit("请以管理员身份运行该程序");
    }

    if let Some(v) = common::check_update() {
        warn!("检测到新版本，请手动更新：{}", v);
    }

    let matches = App::new("YAP - 原神自动拾取器")
        .author("Alex-Beng <pc98@qq.com>")
        .about("Genshin Impact Pickup Helper")
        .arg(Arg::with_name("dump")
            .long("dump")
            .required(false)
            .takes_value(true)
            .default_value("0")
            .help("指定起始的index，输出模型预测结果、二值化图像，debug专用"))
        .get_matches();
    let cnt:u32 = matches.value_of("dump").unwrap_or("0").parse::<u32>().unwrap();


    let hwnd = match capture::find_window("原神") {
        Err(s) => {
            common::error_and_quit("未找到原神窗口，请确认原神已经开启");
        },
        Ok(h) => h,
    };
    unsafe { ShowWindow(hwnd, SW_RESTORE); }
    unsafe { SetForegroundWindow(hwnd); }
    common::sleep(1000);

    // get windows size
    let rect = capture::get_client_rect(hwnd).unwrap();
    info!("left = {}, top = {}, width = {}, height = {}", rect.left, rect.top, rect.width, rect.height);
    
    capture::capture_absolute_image(&rect).unwrap().save("test.png").unwrap();


    let mut info: info::PickupInfo;
    if rect.height * 16 == rect.width * 9 {
        info = info::PickupInfo::from_16_9(rect.width as u32, rect.height as u32, rect.left, rect.top);
    } else {
        common::error_and_quit("不支持的分辨率");
    }

    // Pickup 主逻辑
    let mut pickupper = PickupScanner::new(info, String::from("./black_lists.json"));

    pickupper.start(cnt);


}
