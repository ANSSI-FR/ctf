<?php

// Initialize the session
session_start();
 
// Check if the user is already logged in, if yes then redirect him to welcome page
if(!(isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true)){
    header('Location: login.php');
    exit();
}

// Include config file
require_once 'config.php';

// global
define('SERVER_UPLOAD_PATH', __DIR__ . '/upload/' . $_SESSION['user_upload_dir'] . '/');
define('WEB_UPLOAD_PATH', 'http://' . $_SERVER['HTTP_HOST'] . dirname($_SERVER['PHP_SELF']) . '/upload/');

// Core (class)
class Notes
{
    
    private $pdo;

    function __construct()
    {
        $this->pdo = new PDO('mysql:host=' . DB_SERVER . ';dbname=' . DB_NAME . ';charset=utf8mb4', DB_USERNAME, DB_PASSWORD);
        $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $this->pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    }

    public function fetchNotes($user_id)
    {
        $stmt = $this->pdo->prepare('SELECT * FROM notes WHERE user_id = :user_id ORDER BY created DESC');
        $stmt->bindParam(':user_id', $user_id);
        $stmt->execute();
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $result;
    }
    
    public function create($title, $content, $file)
    {
        $datetime = date('Y-m-d H:i:s');
        $stmt     = $this->pdo->prepare('INSERT INTO notes (user_id, title, content, file) VALUES (:user_id, :title, :content, :file)');
        $stmt->bindParam(':user_id', $_SESSION['id']);
        $stmt->bindParam(':title', $title);
        $stmt->bindParam(':content', $content);
        $stmt->bindParam(':file', $file);
        $stmt->execute();
    }
}

// Init core (class)
$notes = new Notes;

// Actions
if (isset($_POST['new'])) {
    $title       = $_POST['title'];
    $content     = $_POST['content'];
    $target_path = '';
    
    // Test if file
    if (!empty($_FILES['file']['name'])) {
        
        // Where are we going to be writing to?
        $target_path .= SERVER_UPLOAD_PATH . basename($_FILES['file']['name']);
        $msg_err = '';
        
        // File information
        $uploaded_name = $_FILES['file']['name'];
        $uploaded_size = $_FILES['file']['size'];
        
        $allowed_types = array(
            IMAGETYPE_PNG,
            IMAGETYPE_JPEG
        );

        $detectedType  = exif_imagetype($_FILES['file']['tmp_name']);
        
        // Is it an image < 100 kb? 
        if (in_array($detectedType, $allowed_types) && ($uploaded_size < 100000)) {
            
            // Can we move the file to the upload folder?
            if (!move_uploaded_file($_FILES['file']['tmp_name'], $target_path)) {
                // No
                $msg_err .= 'Your image was not uploaded.';
            } else {
                chmod($target_path, 0444);
            }
        } else {
            // Invalid file
            $msg_err .= 'Your image was not uploaded. We can only accept JPEG or PNG images < 100 KB.';
        }
    }

    // Everything is ok - create notes
    if(empty($msg_err)){
        $notes->create($title, $content, $target_path);
    }

    header('Location: .' . (empty($msg_err) ? '' : '/?msg=' . $msg_err));
    exit();
}

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Personal Note</title>
        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' href='/static/css/bootstrap.min.css'>
        <script src='/static/js/jquery.min.js'></script>
        <script src='/static/js/bootstrap.min.js'></script>
        <style>
            .container {
                max-width: 780px;
            }
            textarea {
                resize: vertical;    /* allow only vertical stretch */
            }
            body {
                background-color: #f5f7fa;
            }
        </style>
    </head>
    <body>
<!-- Alert box -->
<?php
if (isset($_GET['msg'])):
?> 
            <div class='alert alert-danger'>
                <center>
                    <strong><?= htmlspecialchars($_GET['msg'], ENT_QUOTES, 'UTF-8') ?></strong>
                </center>
            </div>
<?php
endif;
?>
        
        <div class='container'>
            <div class='page-header'>
                <h2>Save my note</h2>
            </div>
            <form role='form' action='index.php' method='POST' enctype='multipart/form-data'>
                <div class='form-group'>
                    <input class='form-control' type='text' placeholder='Title' name='title' maxlength='50' required>
                </div>
                <div class='form-group'>
                    <textarea class='form-control' rows='5' placeholder='What do you have in mind ?' name='content' maxlength='500' autofocus required></textarea>
                </div>
                <div class='btn-group pull-left'>
                    <input type='file' class='form-control-file' id='file' name='file' title='Attach an image'>
                </div>
                <div class='btn-group pull-right'>
                    <button class='btn btn-danger' type='reset'><span class='glyphicon glyphicon-remove'></span> Clear </button>
                    <button class='btn btn-success' name='new' type='submit'><span class='glyphicon glyphicon-send'></span> Save </button>
                </div>
            </form>
        </div>
<?php
if (isset($_SESSION['id'])):
    $fetchedNotes = $notes->fetchNotes($_SESSION['id']);
?>
        <div class='container' id='notes'>
            <div class='page-header'>
                <h2> Previously saved </h2>
            </div>
            <div class='table-responsive'>
                <table class='table table-hover'>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Date</th>
                            <th>Filename</th>
                            <th class='pull-right'>Actions<br></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <!-- Loop over notes -->
<?php
    foreach ($fetchedNotes as $row):
?>
                            <!-- Array Note Info -->
                            <td>
                                <small><a href='#' class='text-primary' id='noteContent' onclick='$("#noteModal<?= $row["id"] ?>").modal("show");'><?= htmlspecialchars(substr($row['title'], 0, 15), ENT_QUOTES, 'UTF-8') ?></a></small>
                            </td>
                            <td><?= date('d/m/Y H:i', strtotime($row['created'])) ?></td>
                            <td>
                                <a title='Get file' href='<?= htmlspecialchars(WEB_UPLOAD_PATH . $_SESSION['user_upload_dir'] . '/' . basename($row['file']), ENT_QUOTES, 'UTF-8') ?>' target='_blank'>
                                    <?= htmlspecialchars(basename($row['file']), ENT_QUOTES, 'UTF-8') ?>
                                </a>
                            </td>
                            <td class='pull-right'>
                                <div class='btn-group'>
                                    <a class='btn btn-default btn-xs' title='Send by email - soon available' href='#'><span class='glyphicon glyphicon-envelope'></span></a>
                                </div>
                            </td>
                            <!-- -->
                        </tr>
                        <!-- Begin modal part -->
                        <div class='modal fade' id='noteModal<?= $row['id'] ?>' tabindex='-1' role='dialog' aria-labelledby='noteModalTitle<?= $row['id'] ?>' aria-hidden='true'>
                            <div class='modal-dialog' role='document'>
                                <div class='modal-content'>
                                    <div class='modal-header'>
                                        <button type='button' class='close' data-dismiss='modal' aria-label='Close'>
                                        <span aria-hidden='true'>&times;</span>
                                        </button>
                                        <h5 class='modal-title' id='noteModalTitle<?= $row['id'] ?>'><?= htmlspecialchars($row['title'], ENT_QUOTES, 'UTF-8') ?></h5>                                        
                                    </div>
                                    <div class='modal-body' style='white-space: pre-line'>
                                        <?= htmlspecialchars($row['content'], ENT_QUOTES, 'UTF-8') ?>
                                    </div>
                                    <div class='modal-footer'>
                                        <button type='button' class='btn btn-secondary' data-dismiss='modal'>Close</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- End modal part -->
<?php
    endforeach;
?>
                    </tbody>
                </table>
            </div>
<?php
endif;
?>
        </div>
    </body>
</html>