import travel.thailand # 모듈이나 패키지만 가능, 클래스를 임포트 할 수 없음

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from import 문에서만 클래스 임포트 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
