<?php
  header('Access-Control-Allow-Origin: *');
  header('Access-Control-Allow-Methods: POST,GET,OPTIONS');
  header('Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept');
  $id = $_POST['id'];
  $mysqli = new mysqli("angularServer", "root", "", "myBase");
  $mysqli -> query("SET NAMES 'utf-8'");
  $usersData = $mysqli -> query("SELECT DISTINCT `id`, `email` FROM `usersData` WHERE `id` = $id");
  if ($usersData) {
    print_r(json_encode(printResult($usersData)));
  }
  $mysqli -> close();

  function printResult($usersData) {
    $str;
    while(($row = $usersData -> fetch_assoc()) != false) { 
      $str = $row["email"];
    }
    return $str;
  }
?>