Name:		texlive-magra
Version:	57373
Release:	2
Summary:	The Magra font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/magra
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the Magra family of fonts designed by
FontFuror, with support for LaTeX and pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/magra
%{_texmfdistdir}/fonts/vf/public/magra
%{_texmfdistdir}/fonts/type1/public/magra
%{_texmfdistdir}/fonts/tfm/public/magra
%{_texmfdistdir}/fonts/map/dvips/magra
%{_texmfdistdir}/fonts/enc/dvips/magra
%doc %{_texmfdistdir}/doc/fonts/magra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
