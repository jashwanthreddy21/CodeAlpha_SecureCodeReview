# 🔐 Code Review Audit - Task 3

## ❌ Vulnerabilities Found

1. **Command Injection**
   - **File**: `vulnerable_app/app.py` line 9
   - **Problem**: Uses `os.popen()` with user input
   - **Fix**: Use `subprocess.run()` with argument list

2. **Insecure Deserialization**
   - **File**: `vulnerable_app/app.py` line 15
   - **Problem**: Uses `pickle.loads()` on untrusted input
   - **Fix**: Replaced with `json.loads()`

3. **Hardcoded Password**
   - **File**: `vulnerable_app/app.py` line 20
   - **Problem**: Plain text secret
   - **Fix**: Store password hash in env var, use `check_password_hash()`

4. **Lack of Input Validation**
   - No checks on input; added `.isalnum()` for host

5. **Debug Mode On**
   - Changed from `debug=True` to `debug=False`

## ✅ Mitigations Applied
- Implemented input sanitization
- Removed dangerous functions (`os.popen`, `pickle`)
- Configured secure password management