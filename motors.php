<?php	


if(isset($_GET['upvar'])){
system("gpio mode 7 out");
system("gpio mode 0 out");
system("gpio mode 2 out");
system("gpio mode 3 out");
system("gpio write 7 1");
system("gpio write 0 0");
system("gpio write 2 0");
system("gpio write 3 1");
}

else if(isset($_GET['downvar'])){
system("gpio mode 7 out");
system("gpio mode 0 out");
system("gpio mode 2 out");
system("gpio mode 3 out");
system("gpio write 7 0");
system("gpio write 0 1");
system("gpio write 2 1");
system("gpio write 3 0");
}

else if(isset($_GET['leftvar'])){
system("gpio mode 7 out");
system("gpio mode 0 out");
system("gpio mode 2 out");
system("gpio mode 3 out");
system("gpio write 7 1");
system("gpio write 0 0");
system("gpio write 2 1");
system("gpio write 3 0");
}

else if(isset($_GET['rightvar'])){
system("gpio mode 7 out");
system("gpio mode 0 out");
system("gpio mode 2 out");
system("gpio mode 3 out");
system("gpio write 7 0");
system("gpio write 0 1");
system("gpio write 2 0");
system("gpio write 3 1");
}

else if(isset($_GET['stopvar'])){
system("gpio mode 7 out");
system("gpio mode 0 out");
system("gpio mode 2 out");
system("gpio mode 3 out");
system("gpio write 7 0");
system("gpio write 0 0");
system("gpio write 2 0");
system("gpio write 3 0");
}

?>