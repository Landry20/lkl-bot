// LKL-web/api/receive.php
<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

$input = json_decode(file_get_contents('php://input'), true);

if (!$input || !isset($input['table'])) {
    echo json_encode(['status' => 'error']);
    exit;
}

$host = 'localhost';
$user = 'root';
$pass = '';
$db   = 'lkl_bot';

$mysqli = new mysqli($host, $user, $pass, $db);
if ($mysqli->connect_error) die(json_encode(['status' => 'db_error']));

$table = $input['table'];
$data  = $input['data'];
$time  = date('Y-m-d H:i:s');

switch ($table) {
    case 'positions':
        $stmt = $mysqli->prepare("INSERT INTO positions (symbol, order_type, lot, entry, sl, tp, reason, datetime, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'OPEN') ON DUPLICATE KEY UPDATE status='OPEN', datetime=?");
        $stmt->bind_param("ssddddsss", $data['symbol'], $data['type'], $data['lot'], $data['entry'], $data['sl'], $data['tp'], $data['reason'], $time, $time);
        break;

    case 'news':
        $stmt = $mysqli->prepare("INSERT INTO announcements (type, currency, event, impact, datetime, bot_decision, bot_reason) VALUES ('live', ?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("ssssss", $data['currency'], $data['event'], $data['impact'], $data['time'], $data['decision'], $data['reason']);
        break;

    case 'analysis':
        $stmt = $mysqli->prepare("INSERT INTO reports (type, title, content, created_at) VALUES ('live_ta', ?, ?, ?)");
        $stmt->bind_param("sss", $data['symbol'], $data['content'], $time);
        break;

    default:
        echo json_encode(['status' => 'unknown_table']);
        exit;
}

$stmt->execute();
echo json_encode(['status' => 'success', 'time' => $time]);
$mysqli->close();
?>