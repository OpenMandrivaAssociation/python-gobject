# https://gitlab.gnome.org/GNOME/pygobject/issues/253#note_317277
# We don't need to ever pass --no-undefined to Meson because it is enabled by
# default (see: b_lundef option) and is automatically disabled on build targets
# (such as modules) that need it to not be set.
%define _disable_ld_no_undefined 1

%define oname   pygobject

%global __provides_exclude_from ^(%{python3_sitelib})/(pygtkcompat|gi/pygtkcompat.py|gi/_gobject/__init__.py|gi/module.py|gi/__init__.py|gi/overrides/GIMarshallingTests.py)
%global __requires_exclude_from ^(%{python3_sitelib})/(pygtkcompat|gi/pygtkcompat.py|gi/_gobject/__init__.py|gi/module.py|gi/__init__.py|gi/overrides/GIMarshallingTests.py)

%global __requires_exclude typelib\\(%%namespaces

%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	Python bindings for GObject Introspection
Name:		python-gobject
Version:	3.38.0
Release:	1
License:	LGPLv2+ and MIT
Group:		Development/Python
Url:		https://www.gnome.org/
Source0:	https://download.gnome.org/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(py3cairo)
BuildRequires:	pkgconfig(python)
Requires:	python3-gobject = %{version}-%{release}
Provides:	python3-gobject3-devel = %{version}-%{release}
Provides:	python-gobject3-devel = %{version}-%{release}
Obsoletes:	python-gobject3-devel < 3.36.1-2
Obsoletes:	python-gobject3 < 3.36.1-2

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package	devel
Group:		Development/C
Summary:	Python-gobject development files

%description	devel
This contains the python-gobject development files, including C
header, pkg-config file.

%prep
%setup -qn %{oname}-%{version}

# drop bundled egg-info
rm -rf *.egg-info/

%build
%meson -Dpython=%{__python3}
%meson_build

%install
%meson_install

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files
%{python3_sitelib}/gi/
%{python3_sitearch}/gi/
%{python3_sitelib}/pygtkcompat/
%{python3_sitearch}/PyGObject-%{version}.egg-info
