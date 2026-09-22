ep["store_id"] = ep["OutletCode"].astype(str).str.strip()
 
# La base ya viene una fila por tienda con columnas Enero, Febrero, Marzo (ICE scores)
ic_feats = ep[["store_id", "Enero", "Febrero", "Marzo"]].copy()
 
ic_months = ic_feats[["Enero", "Febrero", "Marzo"]]
ic_feats["IC_Promedio"]    = ic_months.mean(axis=1)
ic_feats["Delta_IC"]       = ic_feats["Marzo"] - ic_feats["Enero"]   # tendencia Ene→Mar
ic_feats["Volatilidad_IC"] = ic_months.std(axis=1)                   # std entre los 3 meses
 
base = base.merge(ic_feats, on="store_id", how="left")
log(f"Tiendas con IC: {base['Marzo'].notna().sum():,} / {len(base):,} (IDs distintos, mayoría NaN esperado)")
log(f"Tiendas con Delta_IC (>=2 meses): {base['Delta_IC'].notna().sum():,}")
