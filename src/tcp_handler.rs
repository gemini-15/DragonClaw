use tokio::net::{TcpStream, TcpListener};
use std::error::Error;


pub async fn connect(address: &str) -> Result<(), Box<dyn Error>> {
    let stream = TcpStream::connect(address).await?;

    Ok(())
}


pub async fn listener(address : &str) -> Result<(), Box<dyn Error>> {
    let listener = TcpListener::bind(address).await?;

    Ok(())
}




