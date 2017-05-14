<?
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
$img = imagecreatefromjpeg("cancer.JPG");
imagefilter($img, IMG_FILTER_COLORIZE, 13, 13, 21);
header('Content-Type: image/jpeg');
imagejpeg($img, "cancer2.jpg");
imagedestroy($img)
?>