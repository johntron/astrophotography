//! ```cargo
//! [dependencies]
//! dirs = "3.0"
//! ```

use std::fs;
use std::path::Path;

fn main() {
    let home_dir = dirs::home_dir().expect("Failed to get home directory");
    let config_path = home_dir.join(".cargo/config");

    if !config_path.exists() {
        println!("The file ~/.cargo/config does not exist.");
        return;
    }

    let config_content = fs::read_to_string(&config_path)
        .expect("Failed to read ~/.cargo/config");

    let target_string = "[target.aarch64-unknown-linux-gnu]";
    let linker_string = "linker = \"aarch64-linux-gnu-gcc\"";

    if config_content.contains(target_string) && config_content.contains(linker_string) {
        println!("The ~/.cargo/config contains the target linker configuration for aarch64-unknown-linux-gnu.");
    } else {
        println!("The ~/.cargo/config does NOT contain the target linker configuration for aarch64-unknown-linux-gnu.");
    }
}
