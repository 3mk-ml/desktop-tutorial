<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomeWork4</title>
    <style>body{
        width: 50%; 
        margin:auto;
        text-align:center;
        }</style>
</head>
<body>

    <div class="list">
            <h3>1. to calculate your age</h3>
            <h3>2. to arithmetic operations</h3>
            <h3>3. to determine country</h3>
            <h3>4. to change background color</h3>
            <h3>5. to change background of the page to a image</h3>
        <form action="">
            <input type="number" name="choice" min="1" max="5" step="1" required>
            <input type="submit" name="send">
        </form>
    </div>
    
<?php if(isset($_GET["send"])):?>
<style>.list{display: none;} </style>
<?php
switch ($_GET["choice"]): 
        case 1: ?>
        
        <h3>to calculate your age enter birth year</h3>
        <form action="age.php">
            <input type="number" name="year" min="1900" max="2025" step="1" required>
            <input type="submit">
        </form>
<?php break;
        case 2: ?>  
        <div class="list1">
            <h3>a. to calculate a factorial number</h3>
            <h3>b. to calculate the equation z*y/4</h3>
            <h3>c. to find the days of week</h3>
    </div>        
        <form action="arithmetic_operations.php">
            <input type="text" name="option" required>
            <input type="submit" name="send">
        </form>
<?php break;
        case 3:?>
            <form action="countries.php">
                <h3>choose city</h3>
                <select name="city" required>
                    <option value="صنعاء">صنعاء</option>
                    <option value="الرياض">الرياض</option>
                    <option value="القاهرة">القاهرة</option>
                    <option value="دمشق">دمشق</option>
                    <option value="بيروت">بيروت</option>
                    <option value="بغداد">بغداد</option>
                    <option value="الخرطوم">الخرطوم</option>
                </select>
                <input type="submit">
        </form>
<?php break;
        case 4:?>
            <form action="background.php">
                <h3>choose color to change background</h3>
                <select name="color" required>
                    <option value="red">أحمر</option>
                    <option value="green">أخضر</option>
                    <option value="yellow">أصفر</option>
                </select>
                <input type="submit">
        </form>
<?php break;
        case 5:?>
            <style>
                body{
                    background-image:url(img1.jpg);
                    background-repeat:no-repeat;
                    background-size:cover;
                    background-position:center 27%;}
            </style>
<?php   endswitch; endif; ?>
</body>
</html>