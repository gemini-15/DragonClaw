use tokio::net::{TcpStream, TcpListener};
use std::error::Error;


pub async fn connect(address: &str) -> Result<(), Box<dyn Error>> {
    let _stream = TcpStream::connect(address).await?;

    Ok(())
}


pub async fn listener(address : &str) -> Result<(), Box<dyn Error>> {
    let _listener = TcpListener::bind(address).await?;

    Ok(())
}




