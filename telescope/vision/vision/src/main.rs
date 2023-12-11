use libcamera::{camera_manager::CameraManager, logging::LoggingLevel, stream::StreamRole};
use actix_web::{web, App, HttpRequest, HttpServer, Responder};

async fn greet(req: HttpRequest) -> impl Responder {
    let name = req.match_info().get("name").unwrap_or("World");
    format!("Hello {}!", &name)
}


fn camera() {
    let mgr = CameraManager::new().unwrap();

    mgr.log_set_level("Camera", LoggingLevel::Error);

    let cameras = mgr.cameras();

    for i in 0..cameras.len() {
        let cam = cameras.get(i).unwrap();
        println!("Camera {}", i);
        println!("ID: {}", cam.id());

        println!("Properties: {:#?}", cam.properties());

        let config = cam.generate_configuration(&[StreamRole::ViewFinder]).unwrap();
        let view_finder_cfg = config.get(0).unwrap();
        println!("Available formats: {:#?}", view_finder_cfg.formats());
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("Hello World server started");
    camera();
    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(greet))
            .route("/{name}", web::get().to(greet))
    })
        .bind("[::]:8080")?
        .run()
        .await
}