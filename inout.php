<?php
mysql_connect("localhost","blue","blue321") or die(mysql_error());
// Check connection
mysql_select_db("bluedb") or die(mysql_error()); 

$result = mysql_query("SELECT * FROM Users");

echo "<table border='1'>
<tr>
<th>Firstname</th>
<th>Device</th>
<th>Address</th>
<th>Available</th>
</tr>";

while($row = mysql_fetch_array($result))
  {
  echo "<tr>";
  echo "<td>" . $row['Name'] . "</td>";
  echo "<td>" . $row['Device'] . "</td>";
  echo "<td>" . $row['MAC'] . "</td>";
  echo "<td>" . $row['Avail'] . "</td>";
  echo "</tr>";
  }
echo "</table>";
?>

<html>
<body>

<br />
<form action="insert.php" method="post">
Name: <input type="text" name="Name">
Device: <input type="text" name="Device">
MAC: <input type="text" name="MAC">
<input type="submit">
</form>

</body>
</html>
