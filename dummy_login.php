<?php
// dummy_login.php
$correct_user = "admin";
$correct_pass = "secret123";
$message = ""; // Initialize message

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $user = $_POST["username"];
    $pass = $_POST["password"];

    if ($user === $correct_user && $pass === $correct_pass) {
        $message = "Login success";
    } else {
        $message = "Invalid credentials";
    }

    // If this is being called by curl or script (e.g., brute force tool)
    if (!empty($_SERVER['HTTP_USER_AGENT']) && str_contains($_SERVER['HTTP_USER_AGENT'], 'python')) {
        echo $message;
        exit;
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dummy Login</title>
</head>
<body>
    <h2>🧪 Dummy Login Page</h2>

    <form method="POST" action="">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>

        <label>Password:</label><br>
        <input type="password" name="password"><br><br>

        <button type="submit">Login</button>
    </form>

    <p><?php echo $message; ?></p>
</body>
</html>
