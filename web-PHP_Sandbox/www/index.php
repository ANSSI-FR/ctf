<?php
    
    // L2hvbWUvZmxhZy50eHQ=

    if (isset($_GET['args'])){

    	if(!is_array($_GET['args'])){
    		$args = array();
    		$args[] = $_GET['args'];
    	} else {
    		$args = $_GET['args'];
    	}

        for ( $i=0; $i<count($args); $i++ ){
            if (!preg_match('/^[\w\/|\.]*$/', $args[$i])){
                die('<b>preg_match() has just detected invalid characters! ¯\_(ツ)_/¯</b>');
            }
        }
    } else {
        die('<b>Command arguments not found!</b>');
    }

    $command = implode(" ", $args);

    if(preg_match('/^(\/bin\/cat|cat) +[\w\.\/]*$/',$command)){
        echo passthru($command . " 2>&1");
    } else {
        echo 'Only \'cat &lt;file&gt;\' command allowed';
    }
