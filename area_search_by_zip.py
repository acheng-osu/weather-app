from search_by_zip import search_by_zip
import logging
import json

import grpc
import zip_pb2
import zip_pb2_grpc


def area_search():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = zip_pb2_grpc.ZipSearchingStub(channel)

        while True:
            zipCodeInput = input("Please input your 5 digit zip code here: ")
            weather_array = []

            if len(zipCodeInput) == 5:
                radiusInput = int(input("Please input your radius here: "))
                responseString = stub.ZipSearching(zip_pb2.ZipInput(
                    zipCode=zipCodeInput, radius=radiusInput))
                dumpableString = responseString.output.replace("'", '"')
                dumpableStringAsArray = json.loads(dumpableString)
                for zip in dumpableStringAsArray:
                    weather_array.append(search_by_zip(zip))

                return (weather_array, responseString)
            elif zipCodeInput == "x":
                break
            else:
                print("That is not a valid zip code. Please input a valid zip code. \
                      If you would like to exit the search, input x.")


if __name__ == "__main__":
    area_search()
