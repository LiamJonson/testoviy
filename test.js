!DOCTYPE html>
 
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <div id="out"></div>
    <script>
        function getNumLine(n)
        {
            if (n == 1) return n.toString();
            else return getNumLine(n - 1) + " " + n;
        }
 
        document.getElementById("out").innerHTML = getNumLine(5);
    </script>
</body>
</html>
