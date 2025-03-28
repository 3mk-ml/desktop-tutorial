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
<h1>About Us</h1>
    </section>
    
    <section class="about-us">
        <div class="row">
            <div class="about-col">
                <h1>One of the best world`s universities </h1>
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ipsum aut sapiente laudantium debitis odio officiis, ducimus fuga enim molestiae a? Quasi temporibus nesciunt perspiciatis consectetur, veniam, voluptatibus distinctio fugit deserunt est asperiores laudantium, cum corrupti facere officia recusandae id iure.</p>
                <a href="../backend/register.php" class="hero-btn red-btn">Register Now!</a>
            </div>
            <div class="about-col">
                <img src="images/about.jpg">
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