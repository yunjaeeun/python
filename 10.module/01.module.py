# 같은 경로에 있는 모듈만 사용 가능
# import theater_module
# theater_module.price(3)
# theater_module.price_mornig(3)
# theater_module.price_soldier(3)

# import theater_module as mv     # 별칭으로 호출 가능
# mv.price_soldier(3)

# from theater_module import *
# price_soldier(3)