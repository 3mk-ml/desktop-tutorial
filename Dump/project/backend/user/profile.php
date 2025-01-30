<?php
session_start();
require '../config/db.php';

if (!isset($_SESSION['user_id'])) {
    header('Location: ../login.php');
    exit;
}

$user_id = $_SESSION['user_id'];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $date_of_birth = $_POST['date_of_birth'];

    $stmt = $pdo->prepare("UPDATE users SET name = ?, email = ?, date_of_birth = ? WHERE id = ?");
    $stmt->execute([$name, $email, $date_of_birth, $user_id]);

    header('Location: profile.php');
    exit;
}

$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$user_id]);
$user = $stmt->fetch();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <link rel="stylesheet" href="../../frontend/style.css">
</head>
<body>
    <section class="sub-header">
        <nav>
            <a href="../../frontend/index.php"><img src="../../frontend/images/logo2.png"></a>
            <div class="nav-links" id="navLinks">
                <i class="fa fa-times" onclick="hideMenu()"></i>
                <ul>
                    <li><a href="../../frontend/index.php">HOME</a></li>
                    <li><a href="profile.php">PROFILE</a></li>
                    <li><a href="../logout.php">LOGOUT</a></li>
                </ul>
            </div>
            <i class="fa fa-bars" onclick="showMenu()"></i>
        </nav>
        <h1>Profile</h1>
    </section>

    <section class="about-us">
        <div class="row">
            <div class="about-col">
                <form method="POST" action="profile.php">
                    <input type="text" name="name" value="<?= $user['name'] ?>" placeholder="Enter Your Name" required><br>
                    <input type="email" name="email" value="<?= $user['email'] ?>" placeholder="Enter Your Email" required><br>
                    <input type="date" name="date_of_birth" value="<?= $user['date_of_birth'] ?>"><br>
                    <button type="submit" class="hero-btn red-btn">Update Profile</button>
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

    <script src="../../frontend/script.js"></script>
</body>
</html>
