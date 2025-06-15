param([string]$host, [int]$port)
Test-NetConnection -ComputerName $host -Port $port
