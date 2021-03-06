#!/usr/bin/php
<?php
require_once('path.inc');
require_once('get_host_info.inc');
require_once('rabbitMQLib.inc');
require_once('logger.inc');
$logger = new logger("logger.inc");


try {
$client = new rabbitMQClient("testRabbitMQ.ini","testServer");
if (isset($argv[1]))
{
  $msg = $argv[1];
}
else
{
  $msg = "test message";
}


$request = array();
$request[0] = "login";
$request[1] = array("agoldman","bodypillow");

$response = $client->send_request($request);
$logger->log("received",$response);

echo "client received response: ".PHP_EOL;
print_r($response);
echo "\n\n";

echo $argv[0]." END".PHP_EOL;
}
catch (Exception $e) {
	$logger->log("error", $e->geMessage());
}

