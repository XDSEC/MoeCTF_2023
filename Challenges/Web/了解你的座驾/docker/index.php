<!DOCTYPE html>
<head>
	<meta charset="utf-8">

	<style>
		body {
		background: #ffea92;
		margin: 0;
		font-family: "Open Sans", Helvetica Neue, Helvetica, Arial, sans-serif;
		color: #fff;
		padding-left: 240px;
		}
		main {
			margin: 20px;
			position: absolute;
			overflow-y: scroll;
			min-width: 60%;
		}
		/* css 写得真烂 */
		main .helper {
		margin-bottom: 20px;
		background: rgba(0, 0, 0, 0.2);
		color: #ffea92;
		width: 60%;
		position: relative;
		left: 16%;
		transform: (50%, 0);
		padding: 1.2em 2em;
		text-align: center;
		border-radius: 15px;
		font-size: 2em;
		font-weight: bold;
		}
		main .helper span {
		color: rgba(0, 0, 0, 0.8);
		font-size: 0.4em;
		display: block;
		}
		main .helper img {
			margin: 10px;
			border-radius: 5px;
			width: 80%;
			max-width: 600px;
		}
		.menu {
		background: #5bc995;
		height: 100vh;
		width: 240px;
		position: fixed;
		top: 0;
		left: 0;
		z-index: 5;
		outline: none;
		}
		.menu .avatar {
		background: rgba(0, 0, 0, 0.1);
		padding: 2em 0.5em;
		text-align: center;
		}
		.menu .avatar img {
		width: 100px;
		border-radius: 50%;
		overflow: hidden;
		border: 4px solid #ffea92;
		box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.2);
		}
		.menu .avatar h2 {
		font-weight: normal;
		margin-bottom: 0;
		}
		.menu ul {
		list-style: none;
		padding: 0.5em 0;
		margin: 0;
		}
		.menu ul li {
		padding: 0.5em 1em 0.5em 1.3em;
		font-size: 0.95em;
		font-weight: regular;
		background-repeat: no-repeat;
		background-position: left 15px center;
		background-size: auto 20px;
		transition: all 0.15s linear;
		cursor: pointer;
		}
		.menu ul li:hover {
		background-color: rgba(0, 0, 0, 0.1);
		}
		.menu ul li:focus {
		outline: none;
		}
		@media screen and (max-width: 900px) and (min-width: 400px) {
		body {
			padding-left: 90px;
		}
		.menu {
			width: 90px;
		}
		.menu .avatar {
			padding: 0.5em;
			position: relative;
		}
		.menu .avatar img {
			width: 60px;
		}
		.menu .avatar h2 {
			opacity: 0;
			position: absolute;
			top: 50%;
			left: 100px;
			margin: 0;
			min-width: 200px;
			border-radius: 4px;
			background: rgba(0, 0, 0, 0.4);
			transform: translate3d(-20px, -50%, 0);
			transition: all 0.15s ease-in-out;
		}
		.menu .avatar:hover h2 {
			opacity: 1;
			transform: translate3d(0px, -50%, 0);
		}
		@media screen and (max-width: 400px) {
		body {
			padding-left: 0;
		}
		.menu {
			width: 230px;
			box-shadow: 0 0 0 100em rgba(0, 0, 0, 0);
			transform: translate3d(-230px, 0, 0);
			transition: all 0.3s ease-in-out;
		}
		.menu .smartphone-menu-trigger {
			width: 40px;
			height: 40px;
			position: absolute;
			left: 100%;
			background: #5bc995;
		}
		.menu .smartphone-menu-trigger:before,
		.menu .smartphone-menu-trigger:after {
			content: '';
			width: 50%;
			height: 2px;
			background: #fff;
			border-radius: 10px;
			position: absolute;
			top: 45%;
			left: 50%;
			transform: translate3d(-50%, -50%, 0);
		}
		.menu .smartphone-menu-trigger:after {
			top: 55%;
			transform: translate3d(-50%, -50%, 0);
		}
		.menu ul li {
			padding: 1em 1em 1em 3em;
			font-size: 1.2em;
		}
		.menu:focus {
			transform: translate3d(0, 0, 0);
			box-shadow: 0 0 0 100em rgba(0, 0, 0, 0.6);
		}
		.menu:focus .smartphone-menu-trigger {
			pointer-events: none;
		}
		}}
	</style>

</head>
<body>
	<nav class="menu">
		<div class="smartphone-menu-trigger"></div>
	  <header class="avatar">
		<img src = 'moectf.jpg' />
		<h2>Moe Garage</h2>
	  </header>
		<ul>
		<li onclick="submitForm('Dodge Viper')">Dodge Viper</li>
		<li onclick="submitForm('Mazda rx7-FD')">Mazda rx7-FD</li>
		<li onclick="submitForm('Mustang RTR')">Mustang RTR</li>
		<li onclick="submitForm('Nissan gtr r35')">Nissan gtr r35</li>
		<li onclick="submitForm('Toyota ae86 Trueno 4AGE')">Toyota ae86 Trueno 4AGE</li>
		<li onclick="submitForm('BMW E36 325i')">BMW E36 325i</li>
		<li onclick="submitForm('XDU moeCTF Flag')">XDU moeCTF Flag</li>
	  </ul>
	</nav>
	
	<main>
	  <div class="helper">
		<?php
		
			libxml_disable_entity_loader (false);

			$no_selection = '
			<h2>任意选择一台车！</h2>
			<span>点击左侧的选项</span>';

			$carModels = array(
				"Dodge Viper" => '
				<h2>Dodge Viper</h2>
				<img src="Viper.jpg">
				<img src="Viper1.jpg">
				<span>引擎：8.4L V10<br>
				工作方式：自然吸气<br>
				马力：600hp<br>
				最大扭矩：760N·m<br>
				驱动方式：后驱<br>
				整备质量：1535kg<br>
				轴距：2510mm</span>',

				"Mazda rx7-FD" => '
				<h2>Mazda rx7-FD</h2>
				<img src="rx7.jpg">
				<img src="rx7-1.jpg">
				<img src="rx7-2.jpg">
				<span>引擎：1.3L 双转子<br>
				工作方式：双涡轮<br>
				马力：280hp<i>（你懂的）</i><br>
				最大扭矩：320N·m<br>
				驱动方式：后驱<br>
				整备质量：1260kg<br>
				轴距：2446mm</span>',

				"Mustang RTR" => '
				<h2>Mustang RTR</h2>
				<img src="rtr.jpg">
				<img src="rtr1.jpg">
				<span>加装RTR改装套件，因此参数因套件种类而异<br>
				驱动方式：后驱</span>',

				"Nissan gtr r35" => '
				<h2>Nissan gtr r35</h2>
				<img src="r35.jpg">
				<img src="r35-1.jpg">
				<span>引擎：3.8L V6<br>
				工作方式：涡轮增压<br>
				马力：486hp<br>
				最大扭矩：588N·m<br>
				驱动方式：前置四驱<br>
				整备质量：1815kg<br>
				轴距：2780mm</span>',

				"Toyota ae86 Trueno 4AGE" => '
				<h2>Toyota ae86 Trueno 4AGE</h2>
				<img src="86.jpg">
				<img src="86-1.jpg">
				<span>引擎：1.6L L4<br>
				工作方式：自然吸气<br>
				马力：130hp（低配86hp）<br>
				最大扭矩：N/A<br>
				驱动方式：后驱<br>
				整备质量：900kg<br>
				轴距：N/A</span>',

				"BMW E36 325i" => '
				<h2>BMW E36 325i</h2>
				<img src="36.jpg">
				<img src="36-1.jpg">
				<span>引擎：1.8L L6<br>
				工作方式：自然吸气<br>
				马力：192hp<br>
				最大扭矩：245N·m<br>
				驱动方式：后驱<br>
				整备质量：1315kg<br>
				轴距：2700mm</span>',

				"XDU moeCTF Flag" => '
				<h2>XDU moeCTF Flag</h2>
				<img src="o_o.jpg">
				<span>呜呜呜flag掉到根目录里拿不出来惹<br>
				漂移车一般都在原车基础上大幅改装，因此原厂数据仅供参考</span>');

			if (isset($_POST["xml_content"]) && !empty($_POST["xml_content"])) {

				$xmlContent = $_POST["xml_content"];
				$xml = simplexml_load_string($xmlContent);
				
				if (isset($xml->name) && !empty($xml->name)) {
					$name = (string)$xml->name;
		
					
					if (array_key_exists($name, $carModels)) {
						echo $carModels[$name];
					} 
					else {
						echo "<h2>" . $name . " 不存在</h2>";
					}
				} 
				else {
					echo $no_selection;
				}
			}
			else{
				echo $no_selection;
			}
		?>
	  </div>
	</main>

	<script>
		function submitForm(name) {

			var form = document.createElement("form");
			form.method = "post";
			form.action = "index.php";

			var input = document.createElement("input");
			input.type = "hidden";
			input.name = "xml_content";
			input.value = "<xml><name>" + name + "</name></xml>";

			form.appendChild(input);
			document.body.appendChild(form);
			form.submit();
		}
	</script>
</body>