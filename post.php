<?php


error_reporting(0);

include'post.html';
$token = file_get_contents('token.php');
$address = urlencode($_POST['address']);
//address
$latitude = $_POST['latitude'];
//latitude
$comment = urlencode($_POST['comment']);
//comment
$longitude = $_POST['longitude'];
//longitude


$url = "https://api.xixunyun.com/signin?platform=android&version=3.3.3&token=".$token."&entrance_year=0&graduate_year=0"; 
$post_data = "address=".$address."&latitude=".$latitude."&comment=".$comment."&sign_type=0&longitude=".$longitude;

function send_post($url, $post_data) {    
      $postdata = http_build_query($post_data);    
      $options = array(    
            'http' => array(    
                'method' => 'POST',    
                'header' => 'Content-Type: application/x-www-form-urlencoded',    
                'content' => $postdata,    
                'timeout' => 15 * 60 
            )    
        );    
        $context = stream_context_create($options);    
        $result = file_get_contents($url, false, $context);             
        return $result;    
}

echo " \r\n"."<br>";
echo "---------------------------------------------------------------------------------------------------\r\n"."<br>";
print_r(json_decode(send_post($url, $post_data)));
echo "<br>"."---------------------------------------------------------------------------------------------------"."<br>";
echo "now time : ".date("Y-m-d G:H:s",strtotime("+8 hours"));
echo " \r\n"."<br>";
echo "next time : ".date("Y-m-d G:H:s",strtotime("+32 hours")).".";
?>
