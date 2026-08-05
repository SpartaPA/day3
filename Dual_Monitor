최성진(PA_1기)  [오후 4:30]
Ubuntu NVIDIA 듀얼 모니터 설치 안내
대상: 수업실의 동일한 Ubuntu PC

Ubuntu 22.04.5 LTS
Lenovo Legion Pro 5
NVIDIA GeForce RTX 5060 Laptop GPU
공통 MOK 등록 암호(숫자 12자리): 286419735820
이 번호는 Ubuntu 로그인 암호가 아니다. 재부팅 후 파란 화면에서만 사용한다.전제: 이 PC들은 Secure Boot가 켜져 있어 MOK 등록이 반드시 필요하다. 사전 점검에서 확인된 사항이다. 따라서 아래 단계는 하나도 건너뛰지 않고 순서대로 진행한다.

0. 시작 전 준비
0-1. 외부 모니터는 HDMI 포트에 연결한다
이 노트북은 HDMI 포트가 NVIDIA 그래픽카드에 직접 연결되어 있다. USB-C 포트는 CPU 내장 그래픽으로 연결되므로, 반드시 HDMI 포트를 사용한다.
0-2. 터미널을 연다
키보드에서 Ctrl + Alt + T를 누른다.
0-3. Secure Boot 상태를 확인한다
mokutil --sb-stateSecureBoot enabled 가 나오면 정상이다. 그대로 다음으로 진행한다.
예외: SecureBoot disabled 가 나온 경우 BIOS에서 Secure Boot가 꺼진 PC다. 이 안내서는 켜진 상태를 기준으로 작성돼 있어, 그대로 진행하면 2단계에서 오류가 나거나 5단계 파란 화면이 나타나지 않는다.  아래 [ 문제가 생겼을 때 ]를 참조한다.0-4. 관리자 권한을 먼저 인증한다
sudo -vUbuntu 관리자 암호를 물으면 본인의 PC 로그인 암호를 입력한다.

암호를 입력해도 화면에 글자나 별표가 보이지 않는 것이 정상이다.
오류 없이 원래 터미널 화면으로 돌아오면 인증 성공이다.
0-5. 설치할 드라이버 버전을 확인한다
ubuntu-drivers devices출력 중 recommended 라고 표시된 줄의 패키지 이름을 확인해 적어 둔다. 아래 1-B의 nvidia-driver-595-open 자리에 그 이름을 넣는다.
왜 확인하는가: NVIDIA 595 계열은 Ubuntu 26.04용으로 먼저 패키징됐고, 22.04용 백포트는 시점에 따라 저장소에 없을 수 있다. 없는 패키지 이름을 그대로 붙여넣으면 1-B 전체가 실패한다. recommended 로 표시된 버전을 쓰는 것이 가장 안전하다. (RTX 5060은 Blackwell 세대라 570 미만 버전으로는 동작하지 않는다.)

1. 드라이버 설치 (3단계로 나눠 실행)
여러 줄을 한꺼번에 붙여넣지 않는다. 설치 도중 파란색 debconf 대화상자가 뜰 수 있는데, 미리 붙여넣어 대기 중이던 다음 명령의 글자가 그 대화상자에 입력되어 버린다. 아래 A → B → C 순서로, 앞 명령이 완전히 끝난 뒤 다음을 실행한다.1-A. 저장소 갱신
sudo apt update1-B. 드라이버 및 도구 설치
nvidia-driver-595-open 부분은 0-5에서 확인한 이름으로 바꾼다.
sudo apt install -y linux-headers-$(uname -r) mokutil ubuntu-drivers-common x11-xserver-utils mesa-utils nvidia-driver-595-open
이 명령은 5~15분 걸린다. 끝날 때까지 터미널을 닫지 않는다.
설치 도중 Secure Boot 관련 파란 대화상자가 뜨면, 거기서 암호를 새로 만들지 말고 286419735820을 입력한다(두 번 물어봄). 이 대화상자가 떴다면 2단계는 건너뛴다.
대화상자가 뜨지 않았다면 그대로 다음으로 진행한다.
1-C. PRIME을 NVIDIA로 고정
sudo prime-select nvidia이 명령은 HDMI 모니터가 NVIDIA 그래픽카드를 쓰도록 고정한다. 빼면 외부 모니터가 인식되지 않을 수 있다. already nvidia가 나와도 정상이다.

2. MOK 등록 요청
1-B에서 파란 대화상자를 이미 봤다면 이 단계는 건너뛴다.
아래 4줄을 순서대로 실행한다.
mokutil --generate-hash=286419735820 > /tmp/mok-password.hash
sudo mokutil --import /var/lib/shim-signed/mok/MOK.der --hash-file /tmp/mok-password.hash
rm -f /tmp/mok-password.hash
sudo mokutil --list-new마지막 명령 결과로 판단한다.
   결과 조치     인증서 정보가 길게 표시됨 등록 요청 성공. 다음 단계로 진행   아무것도 표시되지 않음 위에 Secure Boot상태 체크를 다시해본다.
3. 절전 차단 설정
이 노트북은 절전에서 깨어날 때 화면이 깨지는 문제가 있다. 뚜껑을 닫았다 열면 화면이 정상 복구되지 않고, 로그아웃해야만 돌아온다. 아래 설정으로 절전 자체를 차단한다. 이 단계를 건너뛰지 않는다.
3-1. 뚜껑 닫기 동작 변경
아래 2줄을 실행한다.
sudo mkdir -p /etc/systemd/logind.conf.d
printf '[Login]\nHandleLidSwitch=lock\nHandleLidSwitchExternalPower=lock\nHandleLidSwitchDocked=lock\n' | sudo tee /etc/systemd/logind.conf.d/10-no-lid-suspend.conf두 번째 명령을 실행하면 방금 저장된 내용이 화면에 그대로 표시된다. 정상이다.
세 줄이 모두 필요한 이유 — logind는 상황에 따라 다른 항목을 본다.
   상황 적용되는 항목     외부 모니터 연결됨 (수업 중 기본 상태) HandleLidSwitchDocked   모니터 없이 전원 어댑터만 연결 HandleLidSwitchExternalPower   모니터도 전원도 없음 (배터리) HandleLidSwitch   셋 중 하나라도 빠지면 그 상황에서 기본값인 절전(suspend)으로 돌아간다.
3-2. 자동 절전 끄기
아래 2줄을 실행한다.
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'
이 2줄은 sudo를 붙이지 않는다. sudo로 실행하면 본인 계정에 적용되지 않는다.
실행 후 아무 메시지도 나오지 않는 것이 정상이다.
설정이 끝나면 뚜껑을 닫아도 절전되지 않고 화면만 잠긴다.

4. 재부팅
열려 있는 작업을 모두 저장한 뒤 실행한다.
sudo reboot

5. 파란 Enroll MOK 화면
재부팅 중 파란 화면이 나오면 다음 순서로 선택한다.

Enroll MOK
Continue
Yes
286419735820 입력
Reboot
주의사항:

286419735820은 Ubuntu 로그인 암호가 아니다.
숫자 키패드를 사용하지 않는다. 키보드 위쪽 숫자열로 12자리를 입력한다.
Invalid password length가 나오면 입력된 숫자가 부족한 것이다. 위쪽 숫자열로 다시 정확히 입력한다.
화면에는 입력한 숫자가 보이지 않는다. 정상이다.
이 화면은 10초 정도만 표시되고 자동으로 넘어간다. 놓쳤다면 아래 "문제가 생겼을 때"를 본다.


6. Ubuntu 부팅 후 확인 = 성공 했으면 모니터 인식되고 듀얼모니터 켜진다.
터미널을 다시 열고 아래를 하나씩 실행한다.
6-1. MOK 확인
sudo mokutil --test-key /var/lib/shim-signed/mok/MOK.der성공 기준: already enrolled
Failed to access the kernel trusted keyring 같은 줄이 먼저 나올 수 있다. 이 줄은 무시하고, 그 아래 already enrolled만 확인하면 된다.6-2. PRIME 확인
prime-select query성공 기준: nvidia
6-3. NVIDIA 드라이버 확인
nvidia-smi성공 기준: RTX 5060과 드라이버 버전이 표 형태로 표시됨
6-4. 모니터 개수 확인
xrandr --listmonitors성공 기준: 맨 윗줄이 Monitors: 2
모니터 이름은 세션 종류에 따라 다르게 나온다. Xorg 세션이면 HDMI-0, eDP-1-1 처럼, Wayland 세션이면 XWAYLAND0, XWAYLAND2 처럼 표시된다. 둘 다 정상이다. 이름은 보지 말고 Monitors: 2 만 확인한다.6-5. 그래픽 가속 확인
glxinfo -B | grep "OpenGL renderer"성공 기준: 결과에 NVIDIA 또는 RTX 5060이 포함됨 실패 신호: llvmpipe 또는 softpipe가 보이면 CPU로 화면을 그리는 상태다.
이전 안내서의 journalctl -b 0 | grep -c DRISWRAST는 참고용으로만 쓴다. 부팅 초기나 일부 앱 때문에 0이 아닌 값이 나와도 실제로는 정상 가속 중인 경우가 있어 단독 판정 기준으로 삼기 어렵다. 판정은 위 glxinfo 결과로 한다.

7. 화면 위치 조절
Ubuntu에서 설정 → 디스플레이로 이동한다.

모니터 그림을 실제 책상 위 배치와 같게 드래그한다.
원하는 화면을 주 디스플레이로 지정한다.
GNOME에는 디스플레이 감지 버튼이 없을 수 있다. 정상 연결된 모니터는 자동으로 표시된다.


문제가 생겼을 때
파란 Enroll MOK 화면을 놓쳤거나 안 나옴
먼저 이미 등록됐는지 확인한다.
sudo mokutil --test-key /var/lib/shim-signed/mok/MOK.der
already enrolled → 등록 완료. 6-2부터 이어서 진행한다.
그 외 → 아래로 대기 중인 요청이 남아 있는지 확인한다.
sudo mokutil --list-new
인증서가 표시됨 → 그대로 다시 재부팅하면 파란 화면이 또 나온다.
아무것도 안 나옴 → 2단계 4줄을 다시 실행한 뒤 재부팅한다.
2단계에서 No such file or directory 오류가 남
/var/lib/shim-signed/mok/MOK.der 파일이 아직 없다는 뜻이다. 아래로 확인한다.
ls -l /var/lib/shim-signed/mok/
dkms statusdkms status에 nvidia 항목이 없으면 1-B 설치가 실패한 것이다.
외부 모니터가 안 나옴

HDMI 포트에 연결되어 있는지 확인한다. USB-C 포트는 사용하지 않는다.
PRIME 설정을 확인한다.
prime-select query결과가 nvidia가 아니면 아래를 실행하고 재부팅한다.
sudo prime-select nvidia
sudo rebootnvidia-smi가 드라이버를 못 찾음
MOK 등록이 안 끝났을 때 나타나는 대표 증상이다. 6-1을 먼저 확인한다. already enrolled가 아니면 위의 "파란 Enroll MOK 화면을 놓쳤거나 안 나옴" 절차를 따른다.
뚜껑을 닫으니 여전히 절전됨
설정이 실제로 적용됐는지 확인한다.
cat /etc/systemd/logind.conf.d/10-no-lid-suspend.conf
systemctl show systemd-logind | grep -i lid파일 내용은 맞는데 동작이 다르다면, GNOME Tweaks의 노트북 덮개를 닫을 때 절전 항목이 덮어쓰고 있을 수 있다. 해당 항목을 끈 뒤 재부팅한다.
화면이 깨지거나 잔상이 남음
절전에서 깨어난 뒤 발생했다면 알려진 문제다. 로그아웃 후 다시 로그인하면 복구된다. 재부팅해도 된다. 3단계 절전 차단 설정이 되어 있는지 확인한다.
화면이 매우 느리고 창을 옮길 때 끊김
6-5의 glxinfo 결과를 다시 확인한다. llvmpipe가 보이면 CPU 렌더링 상태다.

공식 참고 문서

Ubuntu NVIDIA 드라이버 설치: https://documentation.ubuntu.com/server/how-to/graphics/install-nvidia-drivers/
Ubuntu Secure Boot / MOK: https://wiki.ubuntu.com/UEFI/SecureBoot
systemd logind.conf 항목 설명: https://www.freedesktop.org/software/systemd/man/latest/logind.conf.html
(편집됨)Ubuntu ServerNVIDIA drivers installationThis page shows how to install the NVIDIA drivers from the command line, using either the ubuntu-drivers tool (recommended), or APT. NVIDIA drivers releases: We package two types of NVIDIA drivers:...
