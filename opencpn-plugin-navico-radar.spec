%global commit 7b24587377ee82954b7f8338630aac9740db365e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner canboat
%global project BR24radar_pi
%global plugin br24radar

Name: opencpn-plugin-navico-radar
Summary: OpenCPN radar plugin for Navico Broadband Radars (BR24, 3G, 4G models)
Version: 3.0
Release: 1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Enhances: opencpn%{_isa}

%description
OpenCPN radar plugin for Navico Broadband Radars (BR24, 3G, 4G models).

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so

%{_datadir}/opencpn/plugins/%{plugin}_pi
