<?php
require_once('logger.inc');
require_once('path.inc');
require_once('get_host_info.inc');
require_once('rabbitMQLib.inc');


$logger = new logger("logger.inc");
if (isset($argv[1]))
{
  $msg = $argv[1];
}
else
{
  $msg = "test message";
}

$logger->log("This should fail!");



?>
