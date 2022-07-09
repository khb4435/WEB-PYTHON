class koreaPkg:
    def detail():
        print("korea")
        
if __name__ == "__main__":
    print("모듈 직접 실행")
    trip_to = koreaPkg
    trip_to.detail()
else:
    print("외부에서 이 모듈 실행")