<?php
    $factorial = 1;
    if(isset($_GET["number"])){
        for ($i = 1; $i <= $_GET["number"]; $i++) {
            $factorial *= $i;
        };
        echo "factorial of number $_GET[number]  = ". $factorial;
    };
    
    if(isset($_GET["number1"]) && isset($_GET["number2"])){
        echo "($_GET[number1] * $_GET[number2] / 4)  =  ". $_GET["number1"] * $_GET["number2"] / 4;
        };
        
    $days=["saturday","sunday","monday","tuesday","wednesday","thursday","friday"];
    if(isset($_GET["number3"])){
        echo $days[$_GET["number3"]-1];
    };
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>arithmetic operations</title>
    <style>body{
        width: 50%; 
        margin:auto;
        text-align:center;
        }</style>
</head>
<body>
    
    <?php if(isset($_GET['option'])): ?>
    <style>.list1{display: none;} </style>
<?php   $_GET['option'] = strtolower($_GET['option']);
if($_GET['option']==="a") :?>
                <h3>enter a number to calculate factorial</h3>
                <form action="">
                    <input type="number" name="number" min="1" max="1000000" step="1" required>
                    <input type="submit" name="send">
                </form>
    <?php 
            elseif ($_GET["option"]==="b"):?>
                <p>to calculate the equation z*y/4</p>
                <form action="">
                <p>enter value of z variable</p>
                    <input type="number" name="number1" min="1" max="1000000" step="1" required>
                <p>enter value of y variable</p>
                    <input type="number" name="number2" min="1" max="1000000" step="1" required>
                    <br><br>
                    <input type="submit" name="send">
                </form>
        <?php 
                elseif ($_GET["option"]==="c"):?>
                    <form action="">
                        <h3>enter number between 1 - 7</h3>
                        <input type="number" name="number3" min="1" max="7" step="1" required>
                        <input type="submit" name="send">
                    </form>
        <?php   else:
                    echo "this is choice not one of the options";
        endif;    
                endif; ?>

    
</body>
</html>