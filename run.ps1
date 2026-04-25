$server = Start-Process -FilePath "python" -ArgumentList "-m", "uvicorn", "main:app", "--reload" -WindowStyle Hidden -PassThru
Write-Host "Server started. Waiting for it to initialize..."
Start-Sleep -seconds 15
Write-Host "Testing API..."
python test_api.py
Write-Host "Stopping server..."
Stop-Process -Id $server.Id