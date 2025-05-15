import requests
from art import tprint
from colorama import Fore

def get_ip_info(ip="141.0.12.142") -> str:
    if ip == "":
        ip = "141.0.12.142"
    response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
    
    info = f"""
{Fore.YELLOW}Ip: {Fore.GREEN}{response.get("query")}\n\n{Fore.YELLOW}Country: {Fore.GREEN}{response.get("country")}\n{Fore.YELLOW}Region:{Fore.GREEN} {response.get("region")}\n{Fore.YELLOW}Region Name: {Fore.GREEN}{response.get("regionName")}\n{Fore.YELLOW}City: {Fore.GREEN}{response.get("city")}
{Fore.YELLOW}Lat: {Fore.GREEN}{response.get("lat")}\n{Fore.YELLOW}Lon: {Fore.GREEN}{response.get("lon")}\n{Fore.YELLOW}TimeZone: {Fore.GREEN}{response.get("timezone")}\n{Fore.YELLOW}Provider: {Fore.GREEN}{response.get("isp")}{Fore.RESET}
    """
    print(Fore.RED)
    tprint("GetIpInfo")
    print(Fore.RESET)
    return info


def main():
    ip = input("Enter the IP: ")
    return (get_ip_info(ip=ip))


if __name__ == "__main__":
    print(main())