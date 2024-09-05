# Usa una imagen base de .NET SDK 8.0 para compilar la aplicación
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["backpelis.csproj", "./"]
RUN dotnet restore "./backpelis.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "backpelis.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "backpelis.csproj" -c Release -o /app/publish

# Usa una imagen base de .NET 8.0 para ejecutar la aplicación
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "backpelis.dll"]
