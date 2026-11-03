from pathlib import Path
import plistlib
import re
import sys

app = Path(sys.argv[1])
# Personal signing cannot retain the official app's Associated Domains capability.
(app / "ios/Runner/Runner.entitlements").write_bytes(plistlib.dumps({}))
for name in ["Info-Debug.plist", "Info-Release.plist"]:
    path = app / "ios/Runner" / name
    data = plistlib.loads(path.read_bytes())
    data["CFBundleDisplayName"] = "OpenStop Test"
    data["CFBundleURLTypes"] = [{"CFBundleURLSchemes": ["network.vee.openstop.test"]}]
    path.write_bytes(plistlib.dumps(data))
project = app / "ios/Runner.xcodeproj/project.pbxproj"
text = project.read_text()
text = re.sub(r'PRODUCT_BUNDLE_IDENTIFIER = [^;]+;', 'PRODUCT_BUNDLE_IDENTIFIER = network.vee.openstop.test;', text)
text = re.sub(r'CODE_SIGN_STYLE = [^;]+;', 'CODE_SIGN_STYLE = Automatic;', text)
text = re.sub(r'(?:"DEVELOPMENT_TEAM\[sdk=iphoneos\*\]"|DEVELOPMENT_TEAM) = [^;]+;', 'DEVELOPMENT_TEAM = "";', text)
text = re.sub(r'^\s*(?:"CODE_SIGN_IDENTITY\[sdk=iphoneos\*\]"|CODE_SIGN_IDENTITY|"PROVISIONING_PROFILE_SPECIFIER\[sdk=iphoneos\*\]"|PROVISIONING_PROFILE_SPECIFIER) = [^;]+;\n', '\n', text, flags=re.M)
text = text.replace('buildSettings = {', 'buildSettings = {\n\t\t\t\tCODE_SIGNING_ALLOWED = NO;\n\t\t\t\tCODE_SIGNING_REQUIRED = NO;')
project.write_text(text)
