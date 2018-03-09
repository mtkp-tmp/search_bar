#! Основной файл, выполняющий сборку проекта
import upload_data
import calculations
import output_info


def main():
    coord1 = float(input("Введите первую координату:"))
    coord2 = float(input("Введите вторую координату:"))
    output_info.output_info(calculations.calculations(coord1, coord2, upload_data.upload_data()))
if __name__ == "__main__":
    main()
