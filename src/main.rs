use tokio;
use std::error::Error;

mod tcp_handler;
mod cli;

use tcp_handler::{connect, listener};
use cli::{runDragonClaw};



#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let _cmd = clap::Command::new("dc")
        .bin_name("dragon_claw");

    println!("Hello world");
    Ok(())
}