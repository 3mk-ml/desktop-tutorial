<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sana'a University</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <section class="header">
        <nav>
            <a href="index.php"><img src="images/logo2.png"></a>
            <div class="nav-links" id="navLinks">
                <i class="fa fa-times" onclick="hideMenu()"></i>
                <ul>
                    <li><a href="index.php">HOME</a></li>
                    <li><a href="about.php">ABOUT</a></li>
                    <li><a href="course.php">COURSES</a></li>
                    <li><a href="../backend/login.php"><?php echo isset($_SESSION['user_id']) ? 'LOGOUT' : 'LOGIN'; ?></a></li>
                    <li><a href="contact.php">CONTACT</a></li>
                </ul>
            </div>
            <i class="fa fa-bars" onclick="showMenu()"></i>
        </nav>
        <div class="text-box">
            <h1>Yemen's Biggest University</h1>
            <p>This is Abdullah abdulkareem mufadhl's project. <br>It is done by HTML, CSS, and JS.</p>
            <a href="" class="hero-btn">Visit us to know more</a>
        </div>
    </section>
<section class="course">
    <h1>Courses we offer</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus, excepturi.</p>
    <div class="row">
        <div class="course-col">
            <h3>Intermediate</h3>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque molestias ratione quam a accusamus, dolorum natus consequatur! Dolore, libero quae? Eius delectus ipsam quia odit expedita possimus unde eligendi ex.</p>
        </div>
        <div class="course-col">
            <h3>Degree</h3>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque molestias ratione quam a accusamus, dolorum natus consequatur! Dolore, libero quae? Eius delectus ipsam quia odit expedita possimus unde eligendi ex.</p>
        </div>
        <div class="course-col">
            <h3>Post Graduation</h3>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque molestias ratione quam a accusamus, dolorum natus consequatur! Dolore, libero quae? Eius delectus ipsam quia odit expedita possimus unde eligendi ex.</p>
        </div>
    </div>
</section>
<section class="compus">
    <h1>Our Branches</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe, repudiandae?</p>
    <div class="row">
    <div class="compus-col">
        <img src="images/london.png">
        <div class="layer">
            <h3>SANA'A</h3>
        </div>
           
    </div>
    <div class="compus-col">
        <img src="images/newyork.png">
        <div class="layer">
            <h3>TAIZ</h3>
        </div>
</div>
<div class="compus-col">
    <img src="images/washington.png">
    <div class="layer">
        <h3>ADEN</h3>
    </div>
    </div>
    </div>
</section>
<section class="facilities">
    <h1>Our Facilities</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Inventore, libero?</p>
    <div class="row">
        <div class="facilities-col">
            <img src="images/library.png">
            <h3>Huge library</h3>
            <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Porro voluptates id est perferendis ratione soluta?</p>
        </div>
        <div class="facilities-col">
                <img src="images/basketball.png">
                <h3>Sport Halls</h3>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Porro voluptates id est perferendis ratione soluta?</p>
         </div>
          <div class="facilities-col">
                    <img src="images/cafeteria.png">
                    <h3>Healthy Food</h3>
                    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Porro voluptates id est perferendis ratione soluta?</p>
           </div>
    </div>
</section >
   
    


<section class="cta">
    <h1>Enroll for our variuos online courses<br>Anywhere from the world</h1>
    <a href="contact.html" class="hero-btn">CONTACT US</a>
</section>


<section class="footer">
    <h4>About Us</h4>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit sunt, ab architecto odio distinctio tenetur<br> cumque autem animi tempore nihil! Voluptatum architecto magnam vel qui?</p>
    
    <div class="icons">
        <i class="fa fa-phone"></i>
        <i class="fa fa-twitter"></i>
        <i class="fa fa-instagram"></i>
        <i class="fa fa-linkedin"></i>
    </div>
</section>

    <script src="script.js">
      
    </script>
</body>
</html>
