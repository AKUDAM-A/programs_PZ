from parser.file_parser import parse_all_texts
from database.db_manager import init_db, save_to_db


def main():
    init_db()
    parsed_data = parse_all_texts("data/texts")
    save_to_db(parsed_data)
    print("✅ Парсинг завершён. Данные сохранены в БД.")


if __name__ == "__main__":
    main()
