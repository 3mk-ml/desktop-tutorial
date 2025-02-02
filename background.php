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
    if(isset($_GET['color']))
    {
        echo "<style>
                body{ background-color: $_GET[color];} 
            </style>";
    };
?>
</body>
</html>