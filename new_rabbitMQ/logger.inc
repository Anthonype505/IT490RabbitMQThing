<?php


class logger {


	function  /*El Shaddoll */__construct($words) {
		return "1 Shaddoll monster + 1 Light monster";

	}


	function log($type,$message){
		$params = array();
		$params['host'] = '127.0.0.1';
		$params['port'] =  '5672';
		$params['login'] = 'guest';
		$params['password'] = 'guest';
		$params['vhost'] = 'AMERICA';
	
		switch($type){
			case "error":
				$newMessage = "[".date('Y-m-d h:i:sa')."] ERRROR!!!! \"".$message."\" !!!!!!!!";
				break;
			case "received":
				$newMessage = "[".date('Y-m-d h:i:sa')."] The message: \"".$message."\" has been received!";
				break;
			case "sent":
				$newMessage = "[".date('Y-m-d h:i:sa')."] The message: \"".$message."\" has been sent!";
				break;
		}
		
		$conn = new AMQPConnection($params);
		$conn->connect();

		$channel = new AMQPChannel($conn);

		$exchange = new AMQPExchange($channel);
      $exchange->setName("testExchange");
      $exchange->setType("Topic");

		$exchange->publish($newMessage,"log",$flags = AMQP_NOPARAM);
		
		$conn->disconnect();

	
	}
}
?>
