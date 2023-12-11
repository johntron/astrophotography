//! ```cargo
//! [dependencies]
//! dirs = "3.0"
//! duct = "0.13.6"
//! shlex = "1.2.0"
//! ```

extern crate duct;
extern crate shlex;

use std::fs;
use std::io::Write;
use std::path::Path;
use std::env;
use std::process::Command;
use duct::cmd;
use shlex::split;

fn set_linker() {
    let home_dir = dirs::home_dir().expect("Failed to get home directory");
    let config_path = home_dir.join(".cargo/config");

    if !config_path.exists() {
        fs::OpenOptions::new()
            .create(true)
            .write(true)
            .open(&config_path)
            .expect("Failed to create ~/.cargo/config");
        println!("Created ~/.cargo/config.");
    }

    let mut config_content = fs::read_to_string(&config_path).expect("Failed to read ~/.cargo/config");

    let target_string = "[target.aarch64-unknown-linux-gnu]";
    let linker_string = "linker = \"aarch64-linux-gnu-gcc\"";

    let mut modify = false;

    if !config_content.contains(target_string) {
        config_content.push_str("\n");
        config_content.push_str(target_string);
        config_content.push_str("\n");
        modify = true;
    }

    if !config_content.contains(linker_string) {
        config_content.push_str(linker_string);
        config_content.push_str("\n");
        modify = true;
    }

    if modify {
        let mut file = fs::OpenOptions::new()
            .write(true)
            .truncate(true)
            .open(&config_path)
            .expect("Failed to open ~/.cargo/config for writing");

        file.write_all(config_content.as_bytes())
            .expect("Failed to write to ~/.cargo/config");

        println!("Updated ~/.cargo/config with required configurations.");
    }
}

fn cross_compile_libcamera() {
    // git clone https://git.libcamera.org/libcamera/libcamera.git
    // cd libcamera
    // meson setup build
    // ninja -C build install

    // let output = cmd!(split("git clone --depth 1 --branch v0.1.0 https://git.libcamera.org/libcamera/libcamera.git"))
    //     .read()
    //     .expect("Failed to run cmd");

    // println!("{}", output);
}

fn build() {
    // Get the current directory, which should be the root of the Rust project.
    let current_dir = env::current_dir().expect("Failed to get the current directory");

    // Build the Rust project with the specified target.
    let status = Command::new("cargo")
        .args(&["build", "--target=aarch64-unknown-linux-gnu"])//, "--release"])
        .current_dir(&current_dir)
        .status()
        .expect("Failed to run the cargo build command");

    if status.success() {
        println!("Build successful!");
    } else {
        eprintln!("Build failed!");
    }
}

fn main() {
    set_linker();
    // cross_compile_libcamera();
    build();
}
