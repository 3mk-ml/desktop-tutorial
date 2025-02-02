<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>body{
        width: 50%; 
        margin:auto;
        text-align:center;
        }</style>
</head>
<body>
<?php
    $countries = [
        "صنعاء" => "اليمن",
        "الرياض" => "السعودية",
        "القاهرة" => "مصر",
        "دمشق" => "سوريا",
        "بيروت" => "لبنان",
        "بغداد" => "العراق",
        "الخرطوم" => "السودان"
    ];
    if(isset($_GET['city']))
    {
        echo $_GET['city'] . "  عاصمة  " . $countries[$_GET['city']];
    };
?>
</body>
</html>