# Usa una imagen base de .NET SDK 8.0 para compilar la aplicación
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app

# Copia el archivo de proyecto y restaura las dependencias
COPY *.csproj ./
RUN dotnet restore

# Copia el resto del código de la aplicación y compila
COPY . .
RUN dotnet publish -c Release -o /app/publish

# Usa una imagen base de .NET ASP.NET Core Runtime 8.0 para ejecutar la aplicación
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app

# Copia los archivos compilados desde la etapa de construcción
COPY --from=build /app/publish .

# Exponer el puerto 5180
EXPOSE 5180

# Comando para ejecutar la aplicación
ENTRYPOINT ["dotnet", "backpelis.dll"]
