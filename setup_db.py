"""
Idempotent: garante que o database existe antes do migrate rodar.
Necessário porque Render free só permite 1 PG por team, então
compartilhamos a instância com gag-bot-db mas em databases separados.

Usa pg8000 (já está no requirements.txt do projeto) — psycopg2-binary
pode falhar no build do Render por restrições do ambiente.
"""
import os
import sys


def db_exists(cur, name):
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (name,))
    return cur.fetchone() is not None


def main():
    # Lazy imports
    import pg8000.dbapi

    pg_host = os.environ.get("PG_HOST", "dpg-d994vr77f7vs739qfnv0-a")
    pg_port = int(os.environ.get("PG_PORT", "5432"))
    pg_user = os.environ.get("PG_USER", "gagbot")
    pg_pass = os.environ["PG_PASSWORD"]  # obrigatório
    target_db = os.environ.get("TARGET_DB", "vl_site")
    admin_db = os.environ.get("ADMIN_DB", "gag_bot")

    print(f"[setup_db] Conectando ao {admin_db}@{pg_host}…", flush=True)
    conn = pg8000.dbapi.connect(
        host=pg_host, port=pg_port, user=pg_user, password=pg_pass,
        database=admin_db, ssl=True,
    )
    conn.autocommit = True
    cur = conn.cursor()

    if db_exists(cur, target_db):
        print(f"[setup_db] Database '{target_db}' já existe. OK.", flush=True)
    else:
        # CREATE DATABASE não aceita param. Sanitizar nome.
        safe_name = target_db.replace('"', '""')
        print(f"[setup_db] Criando database '{safe_name}'…", flush=True)
        cur.execute(f'CREATE DATABASE "{safe_name}"')
        print(f"[setup_db] ✓ '{safe_name}' criado.", flush=True)

    cur.close()
    conn.close()
    print("[setup_db] done.", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[setup_db] ERRO: {type(e).__name__}: {e}", flush=True)
        sys.exit(1)
