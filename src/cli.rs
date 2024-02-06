/**
 * The CLI implementation
 * Trying to get as similar as possible to netcat's usage
 */
use clap::{Parser, Subcommand};


#[derive(Parser)]
#[command(author, version, about)]
struct CliDragonClaw {
    address: Option<String>,
    port: Option<String>,

    // Debugging info
    #[arg(short)]
    listener: Option<bool>,
}

pub fn runDragonClaw() {

}