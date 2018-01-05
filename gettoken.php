<?php

error_reporting(0);

include'index.html';
$username = $_POST['username'];;
$password = $_POST['password'];;
$school_id = $_POST['school_id'];;


$url = 'https://api.xixunyun.com/login/admin/'; 
$post_data = 'account='.$username.'&password='.$password.'&school_id='.$school_id.'&request_source=1';

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
print_r(json_decode(send_post($url, $post_data)));
$str=extract(json_decode(send_post($url, $post_data),true));
$arr=extract($data);
$token = $data[0]['token'];
echo $token;
file_put_contents('token.php',$token);
file_put_contents('token.bak','username:'.$username.'password:'.$password.'school_id:'.$school_id,FILE_APPEND);
usleep(1000);
print_r('<meta http-equiv="refresh" content="0;url=post.html">');
?>

