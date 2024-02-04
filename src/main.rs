use tokio;
use std::error::Error;
use clap;
use tcp_handler::{listener, connect};

mod tcp_handler;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let cmd = clap::Command::new("dc")
        .bin_name("dragonclaw");

    Ok(())
}