; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "VIT Notes Sorter"
#define MyAppVersion "1.0"
#define MyAppPublisher "60Degrees"
#define MyAppURL "www.60Degrees.com"
#define MyAppExeName "VIT_Notes_Sorter.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{C4F16E95-BED0-46C7-88C6-FDB9CBC5835F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting\LICENSE
InfoAfterFile=D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting\Finish.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting
OutputBaseFilename=VIT Notes Sorter-setup
SetupIconFile=D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked


[Files]
Source: "D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting\VIT_Notes_Sorter.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting\Course_List.csv"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting\icon.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Offline_Projects\GIT Repo's\VIT-Notes-Sorting\VIT_Notes_Sorter.exe"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{commonstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; 

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

