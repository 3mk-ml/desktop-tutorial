<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sana'a university website design - project </title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz:wght@200..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.6.0/css/fontawesome.min.css">
<script src="https://kit.fontawesome.com/4d93cdabab.js" crossorigin="anonymous"></script>

</head>
<body>
    <section class="sub-header">
<nav>
    <a href="index.html"><img src="images/logo2.png"></a>
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
<h1>Contact Us</h1>
    </section>
    <section class="location">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15388.85280495005!2d44.18930770000002!3d15.364935600000008!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1603db967047d0eb%3A0x171fbbccc82806fd!2z2KzYp9mF2LnYqSDYtdmG2LnYp9ih2Iwg2LXZhti52KfYoeKAjtiMINin2YTZitmO2YXZjtmG!5e0!3m2!1sar!2s!4v1726771594319!5m2!1sar!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </section>
   <section class="contact-us">
    <div class="row">
        <div class="contact-col">
            <div>
                <i class="fa fa-home"></i>
                <span>
                    <h5>DAIRY st. </h5>
                    <p>Sana`a, Repuplic Of Yemen</p>
                </span>
            </div>
            <div>
                <i class="fa fa-phone"></i>
                <span>
                    <h5>+967 779788780 </h5>
                    <p>Sutarday To Wedensday, 8Am To 4pm</p>
                </span>
            </div>
            <div>
                <i class="fa fa-envelope-o"></i>
                <span>
                    <h5>abdullahmofadhl0@gmail.com</h5>
                    <p>Email Us </p>
                </span>
            </div>
        </div>
        <div class="contact-col">
            <form action="">
                <input type="text" placeholder="Enter Your Name" required>
                <input type="email" placeholder="Enter Your Email Addres" required>
                <input type="text" placeholder="Enter Your Subject" required>
                <textarea rows="8" placeholder="Message" required>uyt</textarea>
                <button type="submit" class="hero-btn red-btn">Send Message</button>
            </form>


        </div>
    </div>
   </section>


   
    




<section class="footer">
    <h4>About Us</h4>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit sunt, ab architecto odio distinctio tenetur<br> cumque autem animi tempore nihil! Voluptatum architecto magnam vel qui?</p>
    
    <div class="icons">
        <i class="fa fa-facebook"></i>
        <i class="fa fa-twitter"></i>
        <i class="fa fa-instagram"></i>
        <i class="fa fa-linkedin"></i>
    </div>
</section>

<script src="script.js">
      
</script>
</body>
</html>