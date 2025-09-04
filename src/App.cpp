#include "oatpp/web/server/HttpConnectionHandler.hpp"

#include "oatpp/network/Server.hpp"
#include "oatpp/network/tcp/server/ConnectionProvider.hpp"

#include <iostream>

class Handler : public oatpp::web::server::HttpRequestHandler {
public:

  std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
    std::cout << "Hello World!" << std::endl;
    return ResponseFactory::createResponse(Status::CODE_200, "Hello World!");
  }

};

void run() {

  auto router = oatpp::web::server::HttpRouter::createShared();

  router->route("GET", "/hello", std::make_shared<Handler>());

  auto connectionHandler = oatpp::web::server::HttpConnectionHandler::createShared(router);

  auto connectionProvider = oatpp::network::tcp::server::ConnectionProvider::createShared({"localhost", 8000, oatpp::network::Address::IP_4});

  oatpp::network::Server server(connectionProvider, connectionHandler);

  server.run();
}

int main() {

  oatpp::Environment::init();

  run();

  oatpp::Environment::destroy();

  return 0;

}
